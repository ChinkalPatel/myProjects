using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace WebApplication7.Models
{
    public class Order
    {
        [Key]
        public int oid { get; set; }

        public Address add { get; set; }

        public ICollection<OrderDetail> odetails { get; set; }

        public int tprice { get; set; }

        public DateTime otime { get; set; }

        public DateTime dtime { get; set; }

        [ForeignKey("ApplicationUser")]
        public string Un { get; set; }

        public virtual User ApplicationUser { get; set; }
    }
}