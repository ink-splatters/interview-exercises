#include "api/greeting.h"

namespace api
{
std::string Greeting::greet() const {
  return "hello from Greeting app!";
}

std::string greet(const std::string &name) const {
  return "Hello, " + name + "!";
}
}// namespace api