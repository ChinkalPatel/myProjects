using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace WebApplication7.Models
{
    public class OrderDetail
    {
        [Key]
        public int odid { get; set; }

        [ForeignKey("ord")]
        public int oid { get; set; }

        public Order ord { get; set; }

        [ForeignKey("foods")]
        public int fid { get; set; }

        public virtual Food foods { get; set; }

        public int qty { get; set; }
    }
}