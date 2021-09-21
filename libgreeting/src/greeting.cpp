#include "api/greeting.h"

namespace api
{
namespace
{
  const std::string HELLO = "hello from libgreeting";
}// namespace

std::string Greeting::greet() const {
  return HELLO + "!";
}

std::string Greeting::greet(const std::string &name) const {
  return HELLO + ", " + name;
}
}// namespace api