#pragma once

#include <string>

namespace api
{
class Greeting
{
public:
  std::string greet(const std::string &name) const;
  std::string greet() const;
};
}// namespace api
