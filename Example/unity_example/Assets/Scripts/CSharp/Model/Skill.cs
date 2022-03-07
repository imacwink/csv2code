using UnityEngine;
using System.Collections;

namespace ST
{
	public class Skill : CsvData
	{
		private string[] mAllKey = {
			//"技能ID","技能名","技能描述","技能类型"
			"id","name","desc","type"
		};

		private string[,] mDataArray = {
			{"1","冲刺","瞬间移动3个格子，过程中的敌人将受到物理伤害","瞬发"},
			{"2","击退","选择敌方前排将其击退2个格子","瞬发"},
			{"3","眩晕","随机选择敌方将其眩晕5秒钟","前摇2秒"},
			
		};

		private volatile static Skill sInstance = null;
		private static readonly object lockObject = new object();
		private Skill(){}
		public static Skill getInstance()
		{
			if(sInstance == null)
			{
				lock(lockObject)
				{
					if(sInstance == null)
						sInstance = new Skill();
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