#include <cpr/cpr.h>

#include <iostream>
#include <nlohmann/json.hpp>
using json = nlohmann::json;

int main() {
  while (true) {
    auto r = cpr::Get(cpr::Url{"http://localhost:8000"});
    json j = json::parse(r.text);
    std::cout << j << std::endl;
  }

  return 0;
}
