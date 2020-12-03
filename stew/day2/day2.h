#include<string>
#include<vector>
#pragma once

namespace day2{
    
    struct row
    {
        int n1;
        int n2;
        std::string letter;
        std::string pw;
    };
    std::vector<row> str_v_to_struct(const std::vector<std::string> &str_v);
    void solve_p1(const std::vector<std::string> &in_str_v);
    void solve_p2(const std::vector<std::string> &in_str_v);
};
