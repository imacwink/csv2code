using UnityEngine;
using System.Collections;

namespace ST
{
	public class CsvDataManager
	{
		private static readonly object lockObject = new object();
		private CsvDataManager(){}
		public static CsvData getInstance(string className)
		{
			lock(lockObject)
			{
				//genCode
				if(className == "Entity")
				{
					return Entity.getInstance();
				}
				if(className == "Skill")
				{
					return Skill.getInstance();
				}
				return null;
			}
		}
	}
}