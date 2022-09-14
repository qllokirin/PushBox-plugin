import { segment } from "oicq";
import plugin from '../../../lib/plugins/plugin.js'
import { createRequire } from 'module'
import fetch from "node-fetch";
const require = createRequire(import.meta.url)
const { exec, execSync } = require('child_process')
const _path = process.cwd()
var fs = require('fs');
//游戏是否开始
var if_begin = false

export class helltaker extends plugin {
    constructor() {
        super(
            {
                name: 'helltaker',
                dsc: '',
                event: 'message',
                priority: '50',
                rule: [
                    {
                        reg: '^开始推箱子1$',
                        fnc: 'helltaker',
                    },
                    {
                        reg: '^(左|右|上|下)$',
                        fnc: 'move',
                    }
                ]
            }
        )
    }
    async execSync(cmd) {
        return new Promise((resolve, reject) => {
            exec(cmd, { windowsHide: true }, (error, stdout, stderr) => {
                resolve({ error, stdout, stderr })
            })
        })
    }

    async helltaker(e) {
        this.e.reply("游戏开始~")
        if(fs.existsSync("./plugins/PushBox-plugin/resources/helltaker/array")){
            fs.unlinkSync('./plugins/PushBox-plugin/resources/helltaker/array')
        }
        this.e.reply(segment.image(`./plugins/PushBox-plugin/resources/helltaker/关卡1.png`))
        if_begin = true
        return true
    }
    async move(e) {
        if(!if_begin){
            logger.info("还没开始")
            return false
        }
        let cm = `python ./plugins/PushBox-plugin/resources/helltaker/main.py ${e.msg}`
        let ret = await this.execSync(cm)
        if (ret.error != null) {
            logger.error("出错了")
            this.e.reply("出错了,请到控制台查看报错信息")
            console.log(ret)
        }
        this.e.reply(segment.image(`./plugins/PushBox-plugin/resources/helltaker/now.png`))
        if(!fs.existsSync("./plugins/PushBox-plugin/resources/helltaker/array")){
            if_begin = false
            this.e.reply("恭喜通关")
        }
    }
}