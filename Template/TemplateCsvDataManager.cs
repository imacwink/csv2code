using UnityEngine;
using System.Collections;

namespace ST
{
	public class TemplateCsvDataManager
	{
		private static readonly object lockObject = new object();
		private TemplateCsvDataManager(){}
		public static TemplateCsvData getInstance(string className)
		{
			lock(lockObject)
			{
				//genCode
				return null;
			}
		}
	}
}