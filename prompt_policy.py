"""统一处理发往 Dola/豆包上游的生成提示词。"""

from __future__ import annotations

AUTO_EXECUTE_SUFFIX = (
    "【执行规则】严格按照以上提示词和请求参数直接生成视频。"
    "不要向用户询问、确认、复述提示词或要求再次授权；收到请求后立即执行生成。"
)


def build_upstream_prompt(prompt: str, *, duration: int | None = None) -> str:
    """在提交给上游前追加执行规则和明确时长，保留调用方原始提示词内容。"""
    base = str(prompt or "").strip()
    duration_rule = (
        f"本次视频时长必须为 {int(duration)} 秒，不要使用默认时长。"
        if duration else ""
    )
    rules = "\n".join(item for item in (duration_rule, AUTO_EXECUTE_SUFFIX) if item)
    return f"{base}\n\n{rules}" if base else rules
