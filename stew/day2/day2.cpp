#include"day2.h"
#include<algorithm>




std::vector<day2::row> 
day2::str_v_to_struct(const std::vector<std::string> &str_v)
{
    std::vector<day2::row> row_v;
    for (auto &str_row : str_v)
    {
        day2::row row;
        auto str(str_row);

        int len_n1 = str.find("-");
        row.n1 = std::stoi(str.substr(0,len_n1));
        str.erase(0,len_n1+1);

        int len_n2 = str.find(" ");
        row.n2 = std::stoi(str.substr(0,len_n2));
        str.erase(0,len_n2+1);

        row.letter = str.front();
        str.erase(0,3);

        row.pw = str;

        row_v.emplace_back(row);
    }
    return row_v;
    

}

void
day2::solve_p1(const std::vector<std::string> &in_str_v)
{
    auto row_v = str_v_to_struct(in_str_v);

    int num_match = 0;

    for(auto &row : row_v)
    {
        int count = 0;
        for(auto &letter : row.pw)
        {
            count += (letter == row.letter.c_str()[0]) ? 1 : 0;
        }
        num_match += ((count >= row.n1) && (count <= row.n2)) ? 1 : 0;
    }

     printf("Day  2 Part 1 : %i \n", num_match);    
}

void
day2::solve_p2(const std::vector<std::string> &in_str_v)
{
    auto row_v = str_v_to_struct(in_str_v);

    int num_match = 0;

    for(auto &row : row_v)
    {
        int count = 0;
        count += (row.pw[row.n1 - 1] == row.letter.c_str()[0]);
        count += (row.pw[row.n2 - 1] == row.letter.c_str()[0]);

        num_match += (count == 1) ? 1 : 0;
    }

     printf("Day  2 Part 2 : %i \n", num_match);   


}
