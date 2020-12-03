#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>
#include <filesystem>

#include <iostream>

namespace common
{
    namespace fs = std::filesystem;

    fs::path find_git_root()
    {
        fs::path cwd = fs::current_path();


        fs::path my_dir = "";
        fs::path test_dir;
        for(auto &dir : cwd)
        {            
            my_dir/=dir;
            test_dir = my_dir;
            test_dir/=".git";
            if(fs::exists(test_dir))
            {
                break;                
            }
        }


        return my_dir;
    }

    std::vector<std::string> import_input(std::string f_name)
    {

        std::vector<std::string> out_lines;
        std::ifstream ifs(f_name);
        std::string line;
        while(std::getline(ifs, line))
        {
            out_lines.emplace_back(line);
        }
        return out_lines;
    }
} // namespace common
