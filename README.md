# YZU-Network  
**扬州大学校园网自动连接工具**  
*Network of YZU Automatic Connection*  
目前2025.3.30可用，之前其他大佬脚本的都因为校园网更新了，用不了，迫不得已搞了一下。readme基本是AI写的，不会markdown，菜鸡一个

---

## 🚀 **极速入门（小白推荐）**  
1. 前往 [Release页面](https://github.com/affffff1365/YZU-Network/releases) 下载最新压缩包  
2. 解压后双击运行 `先点我！！！！！.bat`  
3. 根据弹窗提示输入：  
   - 学号（如 `24200xxxx`）  
   - 密码（如 `mypassword`）  
   - 服务序号（如`3`，***这个的数字对应的服务商在弹窗有***）  

---

## 💻 **命令行用法**  
### 基础命令格式  
```bash  
login.exe [用户名] [密码] [服务序号]  
```  

### 📝 **参数详解**  
| 参数位置 | 含义       | 格式要求                  | 示例           |  
|----------|------------|--------------------------|----------------|  
| 第1个    | **学号**   | 字符串（含字母时需引号）  | `"24200xxxx"` |  
| 第2个    | **密码**   | 字符串（特殊符号需引号）  | `"mypassword"`  |  
| 第3个    | **服务序号**| 整数（无需引号）          | `3`           |  

### 🌐 **服务类型说明**  
| 服务序号 | 对应服务名称       | 备注                     |  
|----------|--------------------|--------------------------|  
| `1`      | 学校互联网服务     | 默认校园网（不常用）     |  
| `2`      | 联通互联网服务     | 联通宽带用户使用         |  
| `3`      | 移动互联网服务     | 移动宽带用户使用         |  
| `4`      | 电信互联网服务     | 电信宽带用户使用         |  
| `5`      | 校内免费服务       | 仅限校内资源访问         |  

---

## 🌟 **使用示例**  
### 正确用法 ✅  
```bash  
# 使用移动互联网服务  
login.exe "24200xxxx" "mypassword" 3  

# 使用校内免费服务（访问图书馆等）  
login.exe "24200xxxx" "mypassword" 5  
```  
