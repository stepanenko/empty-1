## AngularJS Market App
### from [Codecademy](https://www.codecademy.com/learn/learn-angularjs)

This is our typical workflow when making an AngularJS app:

- ``ng-app`` is used to define the application scope
- ``ng-controller`` is used to define the controller scope
- Adding data to controller will display it in the view
- A module contains the different components of an AngularJS app
- A controller manages the app’s data
- The view automatically changes and displays the updated data
- The page doesn’t need to reload at any point

We’ve used a few directives in this app:
- ng-app
- ng-controller
- ng-repeat
- ng-src
- ng-click

Directives bind behavior to HTML elements. When the app runs,
AngularJS walks through each HTML element looking for directives.
When it finds one, AngularJS triggers that behavior
(like attaching a scope or looping through an array).

At a high level, directives are markers on a DOM element (such as an attribute, element name, comment or CSS class) that tell AngularJS's HTML compiler ($compile) to attach a specified behavior to that DOM element (e.g. via event listeners), or even to transform the DOM element and its children.

AngularJS comes with a set of these directives built-in, like ngBind, ngModel, and ngClass. Much like you create controllers and services, you can create your own directives for AngularJS to use. When AngularJS bootstraps your application, the HTML compiler traverses the DOM matching directives against the DOM elements.
