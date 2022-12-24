using namespace std;
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        for (string &s: strs){
            string key = s;
            sort(key.begin(), key.end());
            map[key].emplace_back(s);
        }
        vector<vector<string>> result;
        for(auto it=map.begin(); it!=map.end(); it++){
            result.emplace_back(it->second);
        }
        return result;
    }
};