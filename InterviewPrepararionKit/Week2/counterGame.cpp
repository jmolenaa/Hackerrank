#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'counterGame' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts LONG_INTEGER n as parameter.
 */

string counterGame(long n) {
    std::vector<size_t> powers_of_two;
    size_t current_power = 1;
    for (int i = 0; i < 64; ++i) {
        powers_of_two.push_back(current_power);
        current_power *= 2;
    }
    size_t number = n;
    int rounds = 0;
    while (number != 1) {
        auto closest_power = lower_bound(powers_of_two.begin(), powers_of_two.end(), number);
        if (*closest_power == number) {
            number = number / 2;   
        }
        else {
            number = number - *(closest_power - 1);            
        }
        rounds += 1;
        // break;
    }
    if (rounds % 2 == 1) {
        return "Louise";
    }
    return "Richard";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string n_temp;
        getline(cin, n_temp);

        long n = stol(ltrim(rtrim(n_temp)));

        string result = counterGame(n);

        fout << result << "\n";
    }

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
