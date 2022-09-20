Feature: checking correct behaviour for gatito endpoint in animales

  Scenario: send a request for gatito and verify response code
     Given a valid user is logged in for gatito
      When the user sends a get request for gatito
      Then the user obtains a 200 OK for gatito
      Then the user obtains miau
