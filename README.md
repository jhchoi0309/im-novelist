# im-poetry

원문의 뜻과 목소리를 지키며 한국어 AI 문체를 다듬는 공용 스킬입니다.

Claude, Gemini, GPT에서 같은 편집 원칙을 사용할 수 있습니다. Agent Skills를 지원하는 도구에는 스킬 폴더를 설치하고, 일반 대화창에는 독립 프롬프트를 붙여 넣습니다. 사용에 API 키나 외부 서비스는 필요하지 않습니다.

## 어떤 글을 다듬나요?

- 말만 바꾸어 반복하는 문장과 문단
- 과장된 도입, 상투적인 감상, 불필요한 마무리
- 동작을 감춘 명사 나열과 불분명한 연결
- 글의 목적과 맞지 않는 획일적인 호흡과 말투

'있다', '것', '수 있다', 부사, 피동문을 금칙어로 취급하지 않습니다. 가능성, 시간, 감정, 인용, 수치, 코드처럼 보존해야 할 내용을 먼저 확인합니다. 에세이·메시지·지원서·보고서·기술 설명을 각각의 목적에 맞게 다듬습니다.

## 바로 쓰기: Claude · Gemini · ChatGPT

1. [독립 프롬프트](prompts/im-poetry.md)의 **전체 내용**을 복사합니다. GitHub 화면에서는 Raw로 열면 편합니다.
2. 새 대화의 첫 메시지에 붙여 넣습니다. 단순히 저장소 URL만 보내는 것보다 전문을 전달하는 편이 확실합니다.
3. 다음 메시지에 편집할 글과 요청을 보냅니다.

```text
아래 글의 AI 어투를 다듬어줘.
사실과 말투는 유지하고, 수정한 글만 보여줘.

[편집할 글]
```

Claude의 프로젝트 지침이나 Gemini의 Gem 지침을 사용하는 경우에도 같은 프롬프트를 넣을 수 있습니다. 서비스별 기능과 파일 접근 방식은 [호환성 안내](docs/compatibility.md)를 참고하세요. 파일을 올렸다는 이유만으로 지침이 자동 적용된다고 가정하지 않습니다.

## Agent Skills로 설치하기

Python 3.10 이상이 필요합니다. 실행 전 코드를 확인할 수 있으며, 설치기는 네트워크를 사용하지 않습니다. 기존 스킬이나 설정 파일을 덮어쓰지 않습니다.

```bash
git clone https://github.com/jhchoi0309/im-poetry.git
cd im-poetry

# 원하는 도구 하나를 선택합니다.
python3 scripts/install.py --target claude
python3 scripts/install.py --target gemini
python3 scripts/install.py --target codex
```

| 도구 | 사용자 설치 위치 | 사용 방법 |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/im-poetry/` | `/im-poetry`와 편집할 글을 전달 |
| Gemini CLI | `~/.gemini/skills/im-poetry/` | `im-poetry`로 다듬어 달라고 요청 |
| Codex | `~/.agents/skills/im-poetry/` | `$im-poetry`와 편집할 글을 전달 |

특정 프로젝트에만 설치하려면 `--project /path/to/project`를 추가하세요. 설치 내용을 미리 확인하려면 `--dry-run`을 추가하세요. Gemini CLI는 `.agents/skills`도 읽으므로 Codex 경로의 공용 스킬을 사용할 수도 있습니다. 설치 위치를 여러 곳에 만들었다면 도구의 우선순위를 확인하세요.

```bash
python3 scripts/install.py --target claude --project /path/to/project --dry-run
```

이미 다른 내용의 `im-poetry` 폴더가 있으면 설치가 중단됩니다. 기존 폴더를 별도 위치에 백업하거나 `--destination /exact/path/im-poetry`로 다른 설치 위치를 지정하세요. `--destination`은 대상 폴더의 정확한 경로입니다.

## 예시

수정 전:

> 오류의 원인을 분석하는 작업을 진행했고, 분석한 결과를 팀원들과 공유했습니다.

수정 후:

> 오류의 원인을 분석하고 결과를 팀원들과 공유했습니다.

다음 문장들은 뜻을 바꾸지 않고 그대로 둘 수 있습니다.

> 원인을 찾으려 했다.
> 실패할 수도 있다.
> 아직 그 사진을 버리지 못했다.

시도를 성공으로, 가능성을 사실로 바꾸거나 감정을 지우는 편집은 피합니다. 모든 예문은 설명용으로 작성했습니다.

## 구조

| 경로 | 용도 |
| --- | --- |
| [SKILL.md](SKILL.md) | 공통 지침과 작업 순서 |
| [references](references) | 패턴·예외, 의미 보존 예시, 장르별 기준 |
| [prompts/im-poetry.md](prompts/im-poetry.md) | 파일 접근이 없는 대화창용 독립 프롬프트 |
| [docs/compatibility.md](docs/compatibility.md) | 서비스별 설치와 사용 범위 |
| [docs/research.md](docs/research.md) | 출처, 근거의 범위, 설계에 반영한 판단 |
| [docs/evaluation.md](docs/evaluation.md) | 평가 방법과 검증 범위 |
| [evals/cases.json](evals/cases.json) | 의미 보존·말투·모호함에 대한 사례 |
| [scripts](scripts) | 설치·프롬프트 생성·구조 검사 |

## 검증과 수정

```bash
python3 scripts/build.py
python3 scripts/check.py
python3 -m unittest discover -s tests -v
```

공통 규칙을 바꿀 때는 `SKILL.md`를 먼저 고치고 프롬프트를 다시 생성하세요. 생성 파일을 따로 편집하지 않습니다. GitHub Actions는 프롬프트 일치 여부, 문서 링크, 패키지 구성, 설치기의 비파괴 동작을 검사합니다. CI에서 모델 API를 호출하지 않습니다.

형식 호환성과 모델의 실제 출력 품질은 구분합니다. 현재 수행한 행동 평가와 아직 실행하지 않은 서비스는 [평가 기록](docs/evaluation.md)에 명시합니다. 문체만으로 AI 작성 여부를 단정하거나 탐지기 통과를 보장하지 않습니다.

## 기여와 라이선스

수정안을 제안할 때 원문, 요청한 문체, 결과, 보존해야 할 의미를 함께 남겨주세요. 개인 정보나 공개 권한이 없는 원고는 포함하지 마세요.

[MIT License](LICENSE). 참고 자료의 저작권은 각 권리자에게 있습니다. 원본 이미지와 책의 본문을 재배포하지 않으며, 공통 원칙과 예문은 이 프로젝트에 맞게 작성했습니다.

English: A provider-neutral Korean prose editing skill. Install the Agent Skills package in Claude Code, Gemini CLI, or Codex, or paste `prompts/im-poetry.md` into a chat. Preserve meaning and voice; edit formulaic phrasing in context.
