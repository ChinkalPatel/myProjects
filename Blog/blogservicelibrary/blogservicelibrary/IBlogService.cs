using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.ServiceModel;
using System.Text;
using System.Threading.Tasks;

namespace blogservicelibrary
{
    [ServiceContract]
    public interface IBlogService
    {
        [OperationContract]
        DataSet readBlogs(string userid);

        [OperationContract]
        string insertBlogs(string userid, string header, string body, DateTime date,string username);

        [OperationContract]
        string updateBlogs(string userid, string header, string body, DateTime date, string username);

        [OperationContract]
        string deleteBlogs(string userid, string header);
    }
}
