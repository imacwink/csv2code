using UnityEngine;
using System.Collections;

namespace ST
{
	public class TemplateClass : TemplateCsvData
	{
		private string[] mAllKey = {
			//TemplateDescKey
			//TemplateRealKey
		};

		private string[,] mDataArray = {
			//TemplateRealData
		};

		private volatile static TemplateClass sInstance = null;
		private static readonly object lockObject = new object();
		private TemplateClass(){}
		public static TemplateClass getInstance()
		{
			if(sInstance == null)
			{
				lock(lockObject)
				{
					if(sInstance == null)
						sInstance = new TemplateClass();
				}
			}
			return sInstance;
		}

		public override void print()
		{
			int row = mDataArray.GetLength(0);
			int column = mDataArray.GetLength(1);

			for(int i = 0; i < row; i++)
			{
				string printData = "Index : " + i + " | Row: ";
				for(int j = 0; j < column; j++)
				{
					printData += (mDataArray[i, j] + " | ");
				}
				Debug.Log(printData);
			}
		}

		public override string[] getKeyArray()
		{
			return mAllKey;
		}

		public override string[,] getDataArray()
		{
			return mDataArray;
		}

		public  override int num()
		{
			return mDataArray.GetLength(0);
		}

		public  override int keynum()
		{
			return mAllKey.Length;
		}

		private int getTypeNum(string typeName)
		{
			for(int i = 0; i < keynum(); i++)
			{
				if(mAllKey[i] == typeName)
				{
					return i;
				}
			}
			return -1;
		}

		public override string get(int num, string typeName)
		{
			int typenum = getTypeNum(typeName);
			if(typenum == -1)
			{
				Debug.Log(typeName + "   " + num + "  error");
				return "-1";
			}
			return mDataArray[num,typenum];
		}
		
		public override int getInt(int num, string typeName)
		{
			string strItm = get(num, typeName);
			return int.Parse(strItm);
		}

		public override float getFloat(int num, string typeName)
		{
			string strItm = get(num, typeName);
			return float.Parse(strItm);
		}
	}	
}