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
    public class CartsController : Controller
    {
        private Model1 db = new Model1();

        // GET: Carts
        [Authorize]
        public ActionResult Index()
        {
            string un = User.Identity.GetUserName();
            var carts = db.Carts.Where(c => c.ApplicationUser.UserName==un );
            
            
            return View(carts.ToList());
        }

        // GET: Carts/Details/5
        public ActionResult Details(string id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            int id1 = Int32.Parse(id);
            Cart cart = db.Carts.Find(id1);
            if (cart == null)
            {
                return HttpNotFound();
            }
            return View(cart);
        }
        [Authorize]
        [HttpPost]
        public ActionResult Add()
        {
            int foodid = Int32.Parse(Request.Form["fid"]);
            string un = User.Identity.GetUserName();
            Cart c1 = db.Carts.Where(ca => ca.fid == foodid && ca.UserName == un).FirstOrDefault();
            if (c1 == null)
            {
                Cart c = new Cart { UserName = User.Identity.GetUserName(), fid = foodid, qty = 1 };
                db.Carts.Add(c);
                db.SaveChanges();
            }
            else
            {
                c1.qty++;
                db.Entry(c1).State = EntityState.Modified;
                db.SaveChanges();
            }
            TempData["msg"] = "<script>alert('Added succesfully');</script>";
            return RedirectToAction("Index","");
        }

        [HttpPost]
        public ActionResult editqp()
        {
            int caid = Int32.Parse(Request.Form["cid"]);
            Cart c = db.Carts.Find(caid);
            if (c == null)
            {
                return HttpNotFound();
            }
            c.qty++;
            db.Entry(c).State = EntityState.Modified;
            db.SaveChanges();
            return RedirectToAction("Index");
        }

        [HttpPost]
        public ActionResult editqm()
        {
            int caid = Int32.Parse(Request.Form["cid"]);
            Cart c = db.Carts.Find(caid);
            if (c == null)
            {
                return HttpNotFound();
            }
            c.qty--;
            db.Entry(c).State = EntityState.Modified;
            db.SaveChanges();
            return RedirectToAction("Index");
        }

        [HttpPost]
        public ActionResult Remove()
        {
            int caid = Int32.Parse(Request.Form["cid"]);
            Cart c = db.Carts.Find(caid);
            db.Carts.Remove(c);
            db.SaveChanges();
            return RedirectToAction("Index");
        }


        // GET: Carts/Create
        public ActionResult Create()
        {
            ViewBag.UserName = new SelectList(db.Users, "UserName", "Password");
            return View();
        }

        // POST: Carts/Create
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "UserName,fid,qty")] Cart cart)
        {
            if (ModelState.IsValid)
            {
                db.Carts.Add(cart);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            ViewBag.UserName = new SelectList(db.Users, "UserName", "Password", cart.UserName);
            return View(cart);
        }

        // GET: Carts/Edit/5
        public ActionResult Edit(string id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            int id1 = Int32.Parse(id);
            Cart cart = db.Carts.Find(id1);
            if (cart == null)
            {
                return HttpNotFound();
            }
            ViewBag.UserName = new SelectList(db.Users, "UserName", "Password", cart.UserName);
            return View(cart);
        }

        // POST: Carts/Edit/5
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "UserName,fid,qty")] Cart cart)
        {
            if (ModelState.IsValid)
            {
                db.Entry(cart).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.UserName = new SelectList(db.Users, "UserName", "Password", cart.UserName);
            return View(cart);
        }

        // GET: Carts/Delete/5
        public ActionResult Delete(string id)
        {
            
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
             int id1 = Int32.Parse(id);
            Cart cart = db.Carts.Find(id1);
            if (cart == null)
            {
                return HttpNotFound();
            }
            return View(cart);
        }

        // POST: Carts/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(string id)
        {
            int id1 = Int32.Parse(id);
            Cart cart = db.Carts.Find(id1);
            db.Carts.Remove(cart);
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
