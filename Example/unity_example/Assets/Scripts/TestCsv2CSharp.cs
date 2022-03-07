using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using ST;

public class TestCsv2CSharp : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        Entity csvEntity = (Entity)CsvDataManager.getInstance("Entity");
        csvEntity.print();

        for (int i = 0; i < csvEntity.num(); i++)
        {
            Debug.Log("ID : " + csvEntity.getInt(i, "id")
                + " | Name : " + csvEntity.get(i, "name")
                + " | Desc : " + csvEntity.get(i, "desc")
                + " | Speed : " + csvEntity.getFloat(i, "speed"));
        }
    }

    // Update is called once per frame
    void Update()
    {
    }
}
