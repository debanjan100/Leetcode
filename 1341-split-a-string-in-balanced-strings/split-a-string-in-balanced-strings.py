class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count,ans = 0,0
        for i in range(len(s)):
            if s[i]== s[0]:
                count+=1
            else:
                count -=1
            
            if count ==0:
                ans+=1
        return ans
#                 int count = 0, ans = 0;
#         for(int i = 0; i<s.length(); i++){
#             if(s[i] == s[0]) count++;
#             else count--;
#             if(count == 0) ans++;
#         }
#         return ans;
#     }
# };
        