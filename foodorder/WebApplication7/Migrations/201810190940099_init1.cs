namespace WebApplication7.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class init1 : DbMigration
    {
        public override void Up()
        {
            AlterColumn("dbo.Orders", "add_mobileno", c => c.String());
        }
        
        public override void Down()
        {
            AlterColumn("dbo.Orders", "add_mobileno", c => c.Int(nullable: false));
        }
    }
}
