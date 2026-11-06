import collections

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Step 1: Augment queries with their original indices
        # This is crucial because we will sort the queries, but the final
        # answer array needs to be in the original query order.
        # Each item will be (query_time, original_index).
        queries_with_indices = []
        for i in range(len(queries)):
            queries_with_indices.append((queries[i], i))

        # Step 2: Sort both logs and augmented queries by time.
        # Sorting logs allows us to use a two-pointer/sliding window efficiently.
        # Sorting queries allows us to process them in increasing order,
        # which simplifies the sliding window logic as time only moves forward.
        logs.sort(key=lambda item: item[1]) # Sort logs by their timestamp
        queries_with_indices.sort(key=lambda item: item[0]) # Sort queries by query_time

        # Initialize the result array to store answers for each query.
        # It will be filled in the original order of queries.
        result = [0] * len(queries)

        # `active_servers_count` will store the count of requests for each server
        # within the current sliding window. Using collections.Counter is efficient
        # for this, as it handles server IDs and their request counts.
        # A server is considered "active" (received a request) if its count > 0.
        active_servers_count = collections.Counter()

        # `left_log_ptr` and `right_log_ptr` are two pointers for the sorted `logs` array.
        # They define the current sliding window of logs relevant to the current query.
        left_log_ptr = 0
        right_log_ptr = 0

        # Step 3: Iterate through the sorted queries using a sliding window approach.
        for query_time, original_index in queries_with_indices:
            # For each query, the time interval is [query_time - x, query_time].
            # `window_start_time` marks the inclusive lower bound of the interval.
            window_start_time = query_time - x

            # Expand the window to the right: Add all logs whose time is less than or equal to `query_time`.
            # We move `right_log_ptr` forward, adding logs to our `active_servers_count`.
            while right_log_ptr < len(logs) and logs[right_log_ptr][1] <= query_time:
                server_id = logs[right_log_ptr][0]
                active_servers_count[server_id] += 1
                right_log_ptr += 1

            # Shrink the window from the left: Remove all logs whose time is strictly less than `window_start_time`.
            # These logs are now outside the current query's interval.
            # We move `left_log_ptr` forward, decrementing counts in `active_servers_count`.
            while left_log_ptr < len(logs) and logs[left_log_ptr][1] < window_start_time:
                server_id = logs[left_log_ptr][0]
                active_servers_count[server_id] -= 1
                # If a server's request count becomes 0, it means it has no active requests
                # within the current window, so we can remove it from `active_servers_count`.
                if active_servers_count[server_id] == 0:
                    del active_servers_count[server_id]
                left_log_ptr += 1

            # Step 4: Calculate the number of zero-request servers for the current query.
            # The number of servers that received at least one request in the current window
            # is simply the number of unique keys in `active_servers_count`.
            num_active_servers = len(active_servers_count)

            # The total number of servers is `n`.
            # So, `n - num_active_servers` gives the count of servers that received no requests.
            result[original_index] = n - num_active_servers

        # Step 5: Return the final result array.
        return result