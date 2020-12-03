#include"day1.h"
#include<algorithm>

std::vector<int> 
day1::str_v_to_int_v(const std::vector<std::string> &str_v)
{
    std::vector<int> int_v;
    for (auto &str : str_v)
    {
        int_v.emplace_back(std::stoi(str));
    }
    return int_v;
}

void
day1::solve_p1(const std::vector<std::string> &in_str_v)
{
    auto in_int_v = day1::str_v_to_int_v(in_str_v);
    std::sort(in_int_v.begin(), in_int_v.end());
    
    const int SUM = 2020;
    int idx_l = 0;
    int idx_h = in_int_v.size() - 1;

    

    int sum = 0;

    while(idx_l != idx_h)
    {
        sum = in_int_v[idx_l] + in_int_v[idx_h];
        if(sum > SUM)
        {
            idx_h--;
        } else if (sum < SUM) {
            idx_l++;
        } else {
            break;
        }        
    }
    printf("Day  1 Part 1 : %i \n", in_int_v[idx_l] * in_int_v[idx_h]);    

}

void
day1::solve_p2(const std::vector<std::string> &in_str_v)
{
    auto in_int_v = day1::str_v_to_int_v(in_str_v);
    std::vector<int> idx(3);

    const int SUM = 2020;


    for (int ii = 0; ii < in_int_v.size(); ii++)
    {
        for (int jj = ii; jj < in_int_v.size(); jj++)
        {
            for (int kk = jj; kk < in_int_v.size(); kk++)
            {
                int sum = in_int_v[ii] + in_int_v[jj] + in_int_v[kk];
                if(sum == SUM)
                {
                    idx[0] = ii;
                    idx[1] = jj;
                    idx[2] = kk;
                    break;
                }
            }
        }
    }

    printf("Day  1 Part 2 : %i \n", in_int_v[idx[0]] * in_int_v[idx[1]] * in_int_v[idx[2]]);    

}
