#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'sumXor' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts LONG_INTEGER n as parameter.
 */
 
 // 4 = 100
 // for 4 works 000, 001, 010, 011
 // 5 = 101
 // for 5 works 000, 010
 // 10 = 1010
 // for 10 works 0000, 0001, 0100, 0101
 // from what I can tell, however many bit of 0 there are in the original number defines how many x's satisfy the condition
 // and it looks like it's the amount of 0 to the power of 2
 // so first we find the amount of 0 bits then do that to the power of 2

long sumXor(long n) {
    long temp_number = n;
    int zero_bits = 0;
    while (temp_number != 0) {
        // we & the number and 1 to isolate the rightmost bit , f.e. 5
        // 5 = 101
        // 5 & 1 == 101 & 001
        // this & gives the result 001, so we don't add the zero bit
        // next we bitshift 5 to the right, which results in 101 >> 1, 10
        // now with 10, we check again with 1, this isolates the 0 at the right, so we increase the zero_bits
        // we continue until we've had all bits
        // at the end we just raise 2 to the number of zero_bits
        if ((temp_number & 1) == 0) { 
            zero_bits += 1;
        }
        temp_number = temp_number >> 1;
    }
    
    return pow(2, zero_bits);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    long n = stol(ltrim(rtrim(n_temp)));

    long result = sumXor(n);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
