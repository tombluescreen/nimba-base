import websrv
import action_classes as acc

master_holder:acc.Holder


# def generate_html(action_holder_register:list[acc.Action_Holder]):
#     ohtml = []
    
#     for ach in action_holder_register:
#         ohtml.append(f"<div>{ach.label}")
#         for hash,action in ach.action_dict.items():
#             ohtml.append(f"<button class=\"ctlbtn\" api-hash=\"{hash}\">{action.label}</button>")
#         ohtml.append("</div>")

#     olhtml = "\n".join(ohtml)
#     finalHtml = f"<div>{olhtml}</div>"
#     print(finalHtml)
#     return finalHtml

if __name__ == "__main__":
    
    def bruh():
        print("so lit")
        return acc.HTML_Change_Item("FUK U WORLD", api_hash="9fe92b689872ac8307af47ac33dee072").to_json()

    testItem1 = acc.Item("Just Data", "yay data", html_id="bean")
    testItem2 = acc.Btn_Item(bruh,"bruh", "so lit")

    testHold1 = acc.Item_Holder("TestH 1", catagory="beans", items=[testItem1, testItem2])


    master_holder = acc.Holder([testHold1])


    websrv.start_webserver(master_holder,True)

   

    