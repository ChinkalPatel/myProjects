using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace blogservicelibrary
{
    public class BlogService : IBlogService
    {
        public DataSet readBlogs(string userid)
        {
            SqlConnection con = new SqlConnection(@"Data Source=(localdb)\ProjectsV13;Initial Catalog=master;Integrated Security=True;Connect Timeout=30;Encrypt=False;TrustServerCertificate=False;ApplicationIntent=ReadWrite;MultiSubnetFailover=False");
            SqlCommand cmd = new SqlCommand();
            cmd.Connection = con;
            cmd.CommandText = "select userid,header,body,time,username from info where userid=@userid";
            cmd.Parameters.AddWithValue("@userid", userid);
            con.Open();
            DataSet ds = new DataSet();
            using (SqlDataReader rdr = cmd.ExecuteReader())
            {
                ds.Tables.Add("info");
                ds.Tables[0].Load(rdr);
            }
            con.Close();
            return ds;
        }

        public string insertBlogs(string userid, string header, string body, DateTime date, string username)
        {
            date = date.Date;
            string insertString = "INSERT INTO info(userid,header,body,date,username) VALUES (@userid,@header,@body,@date,@username)";
            SqlConnection con = new SqlConnection(@"Data Source=(localdb)\ProjectsV13;Initial Catalog=master;Integrated Security=True;Connect Timeout=30;Encrypt=False;TrustServerCertificate=False;ApplicationIntent=ReadWrite;MultiSubnetFailover=False");
            SqlCommand cmd = new SqlCommand(insertString, con);
            cmd.Parameters.AddWithValue("@userid", userid);
            cmd.Parameters.AddWithValue("@header", header);
            cmd.Parameters.AddWithValue("@body", body);
            cmd.Parameters.AddWithValue("@date", date);
            cmd.Parameters.AddWithValue("@username", username);
            int added = 0;
            con.Open();
            added = cmd.ExecuteNonQuery();
            con.Close();
            if (added != 0)
            {
                return "Blog add successfully !";
            }
            else
            {
                return "So Sorry Please Try Again";
            }
        }

        public string updateBlogs(string userid, string header, string body, DateTime date, string username)
        {
            date = date.Date;
            string updateString = "UPDATE info Set header=@header,body=@body,date=@date,username=@username WHERE userId=@userId";
            SqlConnection con = new SqlConnection(@"Data Source=(localdb)\ProjectsV13;Initial Catalog=master;Integrated Security=True;Connect Timeout=30;Encrypt=False;TrustServerCertificate=False;ApplicationIntent=ReadWrite;MultiSubnetFailover=False");
            SqlCommand cmd = new SqlCommand(updateString, con);
            cmd.Parameters.AddWithValue("@Userid", userid);
            cmd.Parameters.AddWithValue("@header", header);
            cmd.Parameters.AddWithValue("@body", body);
            cmd.Parameters.AddWithValue("@date", date);
            cmd.Parameters.AddWithValue("@username", username);
            int updated = 0;
            con.Open();
            updated = cmd.ExecuteNonQuery();
            con.Close();
            if (updated != 0)
            {
                return "Blog Updated Successfully";
            }
            else
            {
                return "So Sorry Please Try Again";
            }
        }

        public string deleteBlogs(string userid, string header)
        {
            
            string deleteString = "DELETE FROM ReminderTable WHERE userId=@userId and header=@header";
            SqlConnection con = new SqlConnection(@"Data Source=(localdb)\ProjectsV13;Initial Catalog=master;Integrated Security=True;Connect Timeout=30;Encrypt=False;TrustServerCertificate=False;ApplicationIntent=ReadWrite;MultiSubnetFailover=False");
            SqlCommand cmd = new SqlCommand(deleteString, con);
            cmd.Parameters.AddWithValue("@Userid", userid);
            cmd.Parameters.AddWithValue("@date", header);
            int deleted = 0;
            con.Open();
            deleted = cmd.ExecuteNonQuery();
            if (deleted != 0)
            {
                return "Blog Deleted Successfully !";

            }
            else
            {
                return "So Sorry Please Try Again";
            }
        }
    }
}
