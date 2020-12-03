#include"common.h"
#include<filesystem>
#include<iostream>
#include<day1.h>
#include<day2.h>


int main(){     

    auto git_dir = common::find_git_root();
    auto inputs_dir = git_dir.append("stew/inputs");

    std::cout << "Found Input folder at: " << inputs_dir << std::endl;

    day1::solve_p1(common::import_input(inputs_dir.string() + "/day1.txt"));
    day1::solve_p2(common::import_input(inputs_dir.string() + "/day1.txt"));

    day2::solve_p1(common::import_input(inputs_dir.string() + "/day2.txt"));
    day2::solve_p2(common::import_input(inputs_dir.string() + "/day2.txt"));
}

