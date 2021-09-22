

#include <catch2/catch.hpp>
#include <greeting/greeting.h>

SCENARIO( "users must be properly greeted", "[greeting]" ) {
  greeting::Greeting g;

  GIVEN ( "an anonymous user") {
    WHEN ("greeting::Greeting::greet()const overload is called") {
      auto the_greeting = g.greet();

      THEN ("greeting should be") {
        REQUIRE(the_greeting == "Hello from libgreeting!");
      }
    }
  }

  GIVEN ("a named user") {
    WHEN ("greeting::Greeting::greet(const string&)const overload is called") {
      auto the_greeting = g.greet("John Doe");

      THEN ("greeting should be") {
        REQUIRE(the_greeting == "Hello from libgreeting, John Doe!");
      }
    }
  }
}
//TEST_CASE("anonymous user is being greeted", "[positive expectations]") {
//
//
//  REQUIRE( g.greet() == "string value" );
//}
