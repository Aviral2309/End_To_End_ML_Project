import sys
import logging

def error_message_detail(error, error_detail:sys):
  _,_,exc_tb = error_detail.exc_info()
  ## will find out whatever exceptions you are getting 
  file_name = exc_tb.tb_frame.f_code.co_filename # get out file name
  #(in the exception handling doc it is given)
  error_message = 'Error occured in python script name [{0}] line number [{1}] error message [{2}]'.format(
   file_name, exc_tb.tb_lineno, str(error)
  ) ## how your message should look like
  return error_message
  ## whenever the error raises call this particular function

class CustomException(Exception): ## create own exception class
  '''
  This means your CustomException inherits from the built-in Exception class.
  So it behaves like a normal Python exception — but you can add extra info or custom behavior.
  '''
  def __inti__(self, error_message, error_detail:sys):
    super().__inti__(error_message) ## initialise the base exception with your error_message
    self.error_message = error_message_detail(error_message, error_detail=error_detail)
    ## this line calls another helper function - which formats your error message nicely
  '''
  This is the constructor, which runs when the exception object is created.
  It takes:
  error_message: the main error message
  error_detail: an object (from the sys module) that contains detailed information about where the error occurred 
  (like filename, line number, etc.)
  '''
    
  def __str__(self):
    return self.error_message
  '''
  This defines how your exception will be printed.
  When you print() or log the exception, it will return the formatted message instead of the default Python traceback.
  '''
  