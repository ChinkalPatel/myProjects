using Microsoft.AspNet.Identity;
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using WebApplication7.Models;

namespace WebApplication7.Controllers
{
    public class OrdersController : Controller
    {
        private Model1 db = new Model1();

        // GET: Orders
        [Authorize]
        public ActionResult Index()
        {
            string un = User.Identity.GetUserName();
            var orders = db.Orders.Where(o => o.Un == un).Include(f=> f.odetails);

            
            return View(orders.ToList());
        }

        // GET: Orders/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Order order = db.Orders.Find(id);
            if (order == null)
            {
                return HttpNotFound();
            }
            return View(order);
        }

        // GET: Orders/Create
        [Authorize]
        public ActionResult Create()
        {
            return View();
        }

        // POST: Orders/Create
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [Authorize]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "add")] Order order)
        {
            if (ModelState.IsValid)
            {
                string un = User.Identity.GetUserName();
                order.Un = un;
                var carts = db.Carts.Where(c => c.UserName == un);
                //order.carts = carts.ToList();

                
                
                int tp = 0;
                foreach (var c in carts)
                {
                    //order.carts.Add(c);
                    tp += (c.foods.price) * c.qty;
                }
                order.tprice = tp;
                order.otime = DateTime.Now;
                order.dtime = DateTime.Now.AddHours(3);

                db.Orders.Add(order);
                db.SaveChanges();

                foreach (var c in carts.ToList())
                {
                    OrderDetail od = new OrderDetail();
                    od.oid = order.oid;
                    od.fid = c.fid;
                    od.qty = c.qty;
                    db.OrderDetails.Add(od);
                    db.SaveChanges();
                    db.Carts.Remove(c);
                    db.SaveChanges();
                }


                return RedirectToAction("Index");
            }

           
            return View(order);
        }

        // GET: Orders/Edit/5
        
        [Authorize]
        public ActionResult Edit()
        {
            string id = Request.QueryString["oid"];
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            int id1 = Int32.Parse(id);
            Order order = db.Orders.Find(id1);
            if (order == null)
            {
                return HttpNotFound();
            }
           
            return View(order);
        }

        // POST: Orders/Edit/5
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "add")] Order order)
        {
            if (ModelState.IsValid)
            {
                string oid = Request.Form["oid"];
                int oi = Int32.Parse(oid);
                Order o = db.Orders.Find(oi);
                o.add = order.add;
                db.Entry(o).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
           
            return View(order);
        }

        // GET: Orders/Delete/5
        [HttpPost]
        [Authorize]
        public ActionResult Delete()
        {
            string id = Request.Form["oid"];
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            int id1 = Int32.Parse(id);
            Order order = db.Orders.Find(id1);
            if (order == null)
            {
                return HttpNotFound();
            }
            db.Orders.Remove(order);
            db.SaveChanges();
            return RedirectToAction("Index");
           
        }

        

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }
    }
}
