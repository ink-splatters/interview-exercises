#pragma once

#include <string>
#include <string_view>

namespace greeting
{
class Greeting
{
public:
  std::string greet(std::string_view) const;
  std::string greet() const;
};
}// namespace greeting
