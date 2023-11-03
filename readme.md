# 华东师大雀华位牌谱转换器

华东师大雀华位牌谱转换器是一个专门为麻将爱好者设计的工具，旨在帮助用户从雀魂官方网站转换牌谱数据为天凤平台可识别的JSON格式。此转换器允许用户保存雀魂对局的详细记录，并在mortal平台上进行复盘和分析。

## 安装步骤

### 1. 安装Tampermonkey

要使用本转换器，首先确保您的浏览器已安装了Tampermonkey扩展。

- Chrome 用户可以在 [Chrome 网上应用店](https://chrome.google.com/webstore/category/extensions)中搜索 Tampermonkey 并安装。
- Firefox 用户可以在 [Firefox Add-ons](https://addons.mozilla.org/)中搜索 Tampermonkey 并安装。

### 2. 安装downloadlogsnaga.user.js脚本

在Tampermonkey扩展安装并启用后，通过以下步骤加载`downloadlogsnaga.user.js`脚本：

- 打开Tampermonkey的仪表板。
- 点击「添加新脚本」。
- 将`downloadlogsnaga.user.js`脚本的代码复制粘贴到编辑器中。
- 保存脚本。

### 3. 下载雀魂牌谱

在脚本安装完成后，进行以下操作：

- 打开[雀魂官方网站](https://mahjongsoul.game.yo-star.com/)并登录您的账户。
- 导航至您想要保存的牌谱链接。
- 在牌谱页面定位到具体对局。
- 按 `S` 键保存整局的天凤JSON文件到您的电脑上。

### 4. 使用牌谱转换器

一旦获取了天凤格式的牌谱文件，进行以下步骤来转换牌谱：

- 克隆或下载本项目到您的本地环境。
- 打开`main.py`文件。
- 修改文件中的文件路径，将其指向您下载的天凤JSON文件。
- 运行`main.py`脚本。

```bash
python main.py
```

### 5. 生成新的牌谱文件

成功运行脚本后，`new_log.json`文件将被创建，您可以在mortal平台上直接使用该文件。

### 6. 解析牌谱

- 登录到mortal平台。
- 导航至自定义JSON解析区域。
- 上传`new_log.json`文件并查看解析结果。

## 注意事项

- 本转换器仅适用于雀魂官方网站的牌谱。
- 确保在使用本转换器时遵守所有适用的法律法规及雀魂官方的使用条款。
- 本项目不存储任何用户数据，所有转换操作均在用户本地环境完成。

## 贡献

如果您有任何改进建议或希望贡献代码，请随时创建issue或提交pull request。

## 许可证

此项目遵循MIT许可证。有关详细信息，请查看`LICENSE`文件。

---

感谢您选择华东师大雀华位牌谱转换器，希望它能助您一臂之力，享受麻将的乐趣！

祝您牌运亨通！
