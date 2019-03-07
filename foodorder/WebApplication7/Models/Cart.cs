using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace WebApplication7.Models
{
    public class Cart
    {
        [Key]
        public int CartId { get; set; }

        [ ForeignKey("ApplicationUser")]
        public string UserName { get; set; }

        public virtual User ApplicationUser { get; set; }

        [ForeignKey("foods")]
        public int fid { get; set; }

        public virtual Food foods { get; set; }

        public int qty { get; set; }


    }
}