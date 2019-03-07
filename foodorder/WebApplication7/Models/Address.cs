using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace WebApplication7.Models
{
    public class Address
    {
        [Required]
        public string name { get; set; }

        [Required(ErrorMessage = "You must provide a phone number")]
        
        [DataType(DataType.PhoneNumber)]
        [RegularExpression(@"^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$", ErrorMessage = "Not a valid phone number")]
        public string mobileno { get; set; }

        
        [Required]
        [DataType(DataType.PostalCode,ErrorMessage ="Please Enter valid Pincode")]
        [RegularExpression(@"[0-9]{6}",ErrorMessage = "Please Enter valid Pincode")]
        public string pincode { get; set; }

        [Required]
        
        public string city { get; set; }

        [Required]
        
       public string state { get; set; }
        [Required]
        public string address_line1 { get; set; }

        public string address_line2 { get; set; }

    }
}