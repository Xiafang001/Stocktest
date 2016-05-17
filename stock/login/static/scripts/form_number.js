function validate_required(field, alerttxt)
{
  with (field)
    {
      if (value==null||value=="")
        {
          alert(alerttxt);
          return false
        }
      else {
          return true
      }
    }
}

function validate_form(thisform)
{
  with (thisform)
    {
      if(validate_required(stock_number, "Stock number can not be null!"==false)
        {
          stock_number.focus();
          return false
        }
    }
}
