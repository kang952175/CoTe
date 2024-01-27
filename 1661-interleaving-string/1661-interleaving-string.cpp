class Solution {
	bool checkInterleave(string& s1, string& s2, string& s3, int i, int j, vector<vector<int>>& checkRes)
	{
		if(checkRes[i][j] > -1) return checkRes[i][j];

		checkRes[i][j] = 1;
		if(i == 0)
		{
			for(int k = 0; k < j; ++k)
			{
				if(s2[k] != s3[k])
				{
					checkRes[i][j] = 0;
					break;
				}
			}
		}
		else if(j == 0)
		{
			for(int k = 0; k < j; ++k)
			{
				if(s1[k] != s3[k])
				{
					checkRes[i][j] = 0;
					break;
				}
			} 
		}
		else
		{
			if(s1[i-1] != s2[j-1])
			{
				if(s3[i+j-1] == s1[i-1])
					checkRes[i][j] =  checkInterleave(s1,s2, s3, i-1, j, checkRes)? 1:0;
				else if(s3[i+j-1] == s2[j-1])
					checkRes[i][j] =  checkInterleave(s1,s2, s3, i, j-1, checkRes)? 1:0;
				else
					checkRes[i][j] = 0;
			}
			else
			{
				if(s3[i+j-1]!= s1[i-1])
					checkRes[i][j] = 0;
				else
					checkRes[i][j] = (checkInterleave(s1,s2, s3, i-1, j, checkRes)|checkInterleave(s1,s2, s3, i, j-1, checkRes))?1:0;
			}
		}
		return checkRes[i][j];
	}

public:
	bool isInterleave(string s1, string s2, string s3) {
		int n1 = s1.size();
		int n2 = s2.size();
		int n3 = s3.size();

		if(n1 + n2 != n3)return false;
		if(n1 == 0 && n2== 0 && n3==0)return true;
		vector<vector<int>> checkRes(n1+1);
		for(int i = 0; i<=n1; i++)
			checkRes[i] = vector<int>(n2+1, -1);

		bool res = checkInterleave(s1, s2, s3, n1, n2, checkRes);
		return res;
	}
};