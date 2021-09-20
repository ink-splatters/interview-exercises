#include <greeting/greeting.h>
#include <optional>
#include <sstream>

namespace greeting
{
namespace
{
  const std::string HELLO = "Hello from libgreeting";

  std::string do_greet(std::optional<std::string_view> name = {}) {
    // TODO: c++20 std::format, is not supported by MacOS clang for now
    std::stringstream ss;
    ss << HELLO << (name ? ", " : "") << (name ? *name : "") << "!";

    return ss.str();
  }
}// namespace

std::string Greeting::greet() const {
  return do_greet();
}

std::string Greeting::greet(std::string_view name) const {
  return do_greet(name);
}
}// namespace greeting