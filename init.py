from rockstar import RockStar

cpp_code = "std::cout << 'Hello world' << std::endl"
rock_it_bro = RockStar(days=500, file_name='helloWorld.cpp', code=cpp_code)
rock_it_bro.make_me_a_rockstar()