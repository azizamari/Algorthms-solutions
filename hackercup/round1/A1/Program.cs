using System;
using System.IO;
using System.Collections.Generic;

namespace A1
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] content = File.ReadAllLines(@".\weak_typing_chapter_2_validation_input.txt");
            int cc=0;
            int t=Convert.ToInt32(content[cc]);
            cc++;
            string[] w=new string[t];
            for(int i=0;i<t;i++){
                w[i]=content[cc+1];
                cc+=2;
            }
            using(StreamWriter sw=File.AppendText("output.txt"))
            {
                var memo=new Dictionary<string,int>();
                for(int j=0;j<t;j++){
                    var c =w[j];
                    int total=0;
                    foreach(var ll in getAllSubstring(c)){
                        if(memo.ContainsKey(ll))
                            total+=memo[ll];
                        else{
                            int count=0;
                            if(!string.IsNullOrEmpty(ll)){
                                var prev=ll[0];
                                foreach (var f in ll)
                                {
                                    if(f!=prev && f!='F'){
                                        count+=1;
                                        prev=f;
                                    }
                                }
                            }
                            memo[ll]=count;
                            total+=count;
                        }
                    }
                    Console.WriteLine("Case #"+(j+1).ToString()+": "+(total%1000000007).ToString());
                    sw.WriteLine("Case #"+(j+1).ToString()+": "+(total%1000000007).ToString()+"\n");
                }
            }
        }
        static List<string> getAllSubstring(string input){
            var stringList = new List<string>();

            for (int i = 0; i < input.Length; i++)
            {
                for (int j = i; j < input.Length; j++)
                {
                    var substring = input.Substring(i, j-i+1);
                    stringList.Add(substring);
                }
            }
            return stringList;
        }
    }
}
