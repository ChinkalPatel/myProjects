using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace WebApplication7.Models
{
    public class Food
    {
        [Key]
        public int fid { get; set; }

        public string fname { get; set; }

        public int price { get; set; }

    }
}