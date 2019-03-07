namespace WebApplication7.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class init : DbMigration
    {
        public override void Up()
        {
            AlterColumn("dbo.Orders", "add_name", c => c.String(nullable: false));
            AlterColumn("dbo.Orders", "add_city", c => c.String(nullable: false));
            AlterColumn("dbo.Orders", "add_pincode", c => c.String(maxLength: 6));
            AlterColumn("dbo.Orders", "add_state", c => c.String(nullable: false));
            AlterColumn("dbo.Orders", "add_address_line1", c => c.String(nullable: false));
        }
        
        public override void Down()
        {
            AlterColumn("dbo.Orders", "add_address_line1", c => c.String());
            AlterColumn("dbo.Orders", "add_state", c => c.String());
            AlterColumn("dbo.Orders", "add_pincode", c => c.Int(nullable: false));
            AlterColumn("dbo.Orders", "add_city", c => c.String());
            AlterColumn("dbo.Orders", "add_name", c => c.String());
        }
    }
}
