import base64
import hashlib

class changeCon():

    xml = '<?xml version="1.0" encoding="gbk"?><business comment="采购合同修改信息" id="BA_CONTRACT_UPDATE">      <group>   ' \
      '           <update_id>%s</update_id>              <rec_id>%s</rec_id>              <con_no>'\
      ' %s</con_no>              <gysmc>%s</gysmc>              ' \
      '<skyh>%s</skyh>              <yhzh>%s</yhzh>       </group>   ' \
      '    <business comment="附件信息" id="BA_CONTRACT_ACCESS">              <group>                     ' \
      '<access_id>%s</access_id>                     <access_name>%s</access_name>        ' \
      '             <access_remark/>                      <access_type>%s</access_type>                      ' \
      '<access_data>%s</access_data>              </group>       </business></business>'



    def conMD5(self, data):

        return hashlib.md5(data.encode()).hexdigest()

    def conBase64(self, filePath):
        with open(filePath,"rb") as f:
            return base64.b64encode(f.read())

    def controlLogic(self):

        filename = input("请输入文件名(请带后缀png,jpg,pdf等)：")
        filetype = input("请输入文件类型(png,jpg,pdf等)：")
        name = input("请随意输入名字，请不要与之前输入的名字重复(任意输入值即可)：")
        path = input("请随意输入路径值，请不要与之前输入的路径重复(任意输入值即可)：")
        updateid = input("请输入update_id(结算单上的备案号)：")
        recordid = input("请输入record_id(同步号)：")
        conno = input("请输入合同号(订单号前加C字符)：")
        gysmc = input("请输入供应商名称：")
        skyh = input("请输入供应商开户行：")
        yhzh = input("请输入供应商银行账户：")


        finalxml = self.xml%(updateid, recordid, conno, gysmc, skyh, yhzh, self.conMD5(path+name), self.conMD5(filename)
                             +"."+filetype, filetype, self.conBase64(filename).decode())
        file = open('./contractChange.log', 'w', encoding='gbk')
        file.write(finalxml)

        input("文件生成成功，请在同级目录查看contractChange.log文件。按回车退出程序")

if __name__ == '__main__':
    a = changeCon()
    a.controlLogic()