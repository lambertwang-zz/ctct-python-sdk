Components package
==================

This package contains components which are subclasses of python dictionaries.  
The components have lambda-generated getter, setter, and deleter methods for basic fields.  
Even readonly fields will have setter and deleter methods.  
Additional setting and retrieval methods are included for fields which require additional logic to be handled.  
It is up to the user to recognize that some components will be invalidated if certain are improperly set.  
Components that are passed other component models through methods will also accept a dict.  
A dict passed this way will be casted to the accepted component class.  
