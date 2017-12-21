using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Contacts
{
    class contact {
        public String phone { get; set; }
        public String name { get; set; }
        public String email { get; set; }

        public contact(String name, String email, String phone){
            this.name = name;
            this.phone = phone;
            this.email = email;
        }
    }

    class Program
    {
        List<contact> ContactList = new List<contact>();

        public Program() {
            addContact("Sheryl", "sheryl.beryl@gmail.com", "0216358285");
            GetInfoByName("Sheryl");
        }

        public void addContact(String name, String email, String phone)
        {
            ContactList.Add(new contact(name, email, phone));
        }

        public void GetInfoByName(String name) {
            foreach(contact c in ContactList) {
                if (c.name==name) {
                    Console.WriteLine(c.email);
                    Console.WriteLine(c.phone);
                    Console.ReadKey();
                }
            }
        }

        static void Main(string[] args)
        {
            new Program();


        }
    }
}