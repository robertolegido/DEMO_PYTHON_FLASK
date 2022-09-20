Feature: checking correct behaviour for perrito endpoint in animales

  Scenario: send a request for perrito and verify response code
     Given a valid user is logged in for perrito
      When the user sends a get request for perrito
      Then the user obtains a 200 OK for perrito
      Then the user obtains guau
