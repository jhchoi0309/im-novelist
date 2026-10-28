# im-novelist

기존 `im-poetry`의 의미 보존·자연스러운 산문 퇴고 기능을 별도 스킬과 저장소로 이어갑니다. 기존 저장소와 로컬 설치본의 삭제는 이 프로젝트의 설치 과정에서 자동 수행하지 않습니다. 문학적·시적 표현을 적극적으로 더하고 싶다면 별도 스킬 [im-poet](https://github.com/jhchoi0309/im-poet)을 사용하세요.

**글의 뜻과 말투를 살리며 AI식 표현을 다듬는 한국어 퇴고 스킬입니다.**

반복되는 설명과 번역투를 정리하면서, 글쓴이가 실제로 하려던 말과 남기고 싶은 표현을 함께 살핍니다. 에세이부터 자기소개서, 메시지, 보고서와 기술 설명까지 글의 목적에 맞춰 사용할 수 있습니다.

Claude, Gemini, GPT에서 같은 편집 원칙을 사용할 수 있습니다. Agent Skills를 지원하는 도구에는 스킬 폴더를 설치하고, 일반 대화창에는 독립 프롬프트를 붙여 넣습니다. 사용에 API 키나 외부 서비스는 필요하지 않습니다.

## im-novelist의 강점

- **의미가 달라지지 않도록 살핍니다.** 시도와 성공, 가능성과 실제 발생, 개인과 팀의 역할을 구분합니다. 수치·날짜·인과관계·평가 조건도 원문과 대조해 함부로 강화하거나 지우지 않도록 합니다.
- **글쓴이의 목소리를 존중합니다.** '아직', '수 있다', 피동문처럼 의미나 감정을 담을 수 있는 표현을 금칙어로 취급하지 않습니다. 에세이의 여백과 망설임, 필요한 긴 문장과 반복도 문맥을 보고 살립니다.
- **문장과 문단을 함께 읽습니다.** 문장 하나의 어색함뿐 아니라 문단 사이의 반복과 연결도 살핍니다. 자기소개서에서는 실제 경험과 판단이 드러나는지 확인하고, 구조 개편을 요청받으면 주어진 근거 안에서 내용을 재배치할 수 있습니다.
- **원하는 말투에 맞춰 조절할 수 있습니다.** 덜 단정적인 표현을 원하면 일상적인 권유를 부드러운 제안으로 다듬거나 일반적인 효과를 가능성으로 표현할 수 있습니다. 이때 주장 강도가 달라질 수 있으며, 실제 사건·측정값·확정 일정과 필수 조건은 흐리지 않도록 합니다.
- **필요한 검토를 골라 요청할 수 있습니다.** 변경 이유를 짧게 설명하거나 분량·블라인드·사실·문서 배치를 추가로 점검할 수 있습니다. 점검은 제공된 기준과 실제 확인할 수 있는 자료의 범위에서 이루어집니다.
- **여러 도구에서 같은 원칙을 쓸 수 있습니다.** Claude Code·Gemini CLI·Codex에는 스킬을 설치하고, 일반 대화창에서는 독립 프롬프트를 복사해 사용할 수 있습니다.

## 이렇게 다듬습니다

| 상황 | 원문 | 가능한 결과 |
| --- | --- | --- |
| 장황한 표현 정리 | 오류의 원인을 분석하는 작업을 진행했고, 분석한 결과를 팀원들과 공유했습니다. | 오류의 원인을 분석하고 결과를 팀원들과 공유했습니다. |
| 시도와 성공 구분 | 원인을 찾으려 했다. | 원인을 찾으려 했다. |
| 감정이 담긴 표현 보존 | 아직 그 사진을 버리지 못했다. | 아직 그 사진을 버리지 못했다. |
| 부드러운 권유 요청 | 경복궁 한번 가봐. | 경복궁 한번 가보는 건 어때? |

두 번째와 세 번째 문장은 그대로 두어도 됩니다. '찾으려 했다'를 '찾았다'로 바꾸면 시도가 성공이 되고, '아직'을 지우면 문장에 담긴 시간과 감정이 달라질 수 있기 때문입니다. 마지막 예시는 덜 단정적인 말투를 요청했을 때 직접적인 권유를 제안으로 바꾼 경우입니다.

예문은 설명을 위해 작성했습니다. 실제 결과는 모델, 원고와 요청에 따라 달라질 수 있습니다.

## 바로 쓰기: Claude · Gemini · ChatGPT

1. [독립 프롬프트](prompts/im-novelist.md)의 **전체 내용**을 복사합니다. GitHub 화면에서는 Raw로 열면 편합니다.
2. 새 대화의 첫 메시지에 붙여 넣습니다. 단순히 저장소 URL만 보내는 것보다 전문을 전달하는 편이 확실합니다.
3. 다음 메시지에 편집할 글과 요청을 보냅니다.

```text
아래 글의 AI 어투를 다듬어줘.
사실과 말투는 유지하고, 수정한 글만 보여줘.

[편집할 글]
```

Claude의 프로젝트 지침이나 Gemini의 Gem 지침을 사용하는 경우에도 같은 프롬프트를 넣을 수 있습니다. 서비스별 기능과 파일 접근 방식은 [호환성 안내](docs/compatibility.md)를 참고하세요. 파일을 올렸다는 이유만으로 지침이 자동 적용된다고 가정하지 않습니다.

## Agent Skills로 설치하기

### 이전 `im-poetry` 설치본에서 이름 바꾸기

새 저장소 이름은 `im-novelist`입니다. 이전 주소에서 받은 로컬 저장소는 원격 주소를 갱신하세요. 설치된 스킬 폴더 이름은 자동으로 바뀌지 않으므로, 기존 설치본은 `--migrate-from`으로 지정합니다. 이전 폴더 전체를 백업하고 새 이름으로 설치합니다. 새 이름의 폴더가 이미 있으면 중단하며, 기존 폴더나 심볼릭 링크를 임의로 덮어쓰지 않습니다.

```bash
git remote set-url origin https://github.com/jhchoi0309/im-novelist.git
python3 scripts/install.py --target claude --migrate-from ~/.claude/skills/im-poetry
python3 scripts/install.py --target gemini --migrate-from ~/.gemini/skills/im-poetry
python3 scripts/install.py --target codex --migrate-from ~/.agents/skills/im-poetry
```

설치했던 도구에 해당하는 명령만 사용하세요. 설치 경로를 따로 지정했다면 실제 이전 경로를 전달하세요. ChatGPT 개인 스킬과 맥의 도구별 설치본은 각각 별개입니다.

### 새로 설치하기

Python 3.10 이상이 필요합니다. 실행 전 코드를 확인할 수 있으며, 설치기는 네트워크를 사용하지 않습니다. 기본 설치에서는 기존 스킬이나 설정 파일을 덮어쓰지 않습니다.

```bash
git clone https://github.com/jhchoi0309/im-novelist.git
cd im-novelist

# 원하는 도구 하나를 선택합니다.
python3 scripts/install.py --target claude
python3 scripts/install.py --target gemini
python3 scripts/install.py --target codex
```

| 도구 | 사용자 설치 위치 | 사용 방법 |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/im-novelist/` | `/im-novelist`와 편집할 글을 전달 |
| Gemini CLI | `~/.gemini/skills/im-novelist/` | `im-novelist`로 다듬어 달라고 요청 |
| Codex | `~/.agents/skills/im-novelist/` | `$im-novelist`와 편집할 글을 전달 |

특정 프로젝트에만 설치하려면 `--project /path/to/project`를 추가하세요. 설치 내용을 미리 확인하려면 `--dry-run`을 추가하세요. Gemini CLI는 `.agents/skills`도 읽으므로 Codex 경로의 공용 스킬을 사용할 수도 있습니다. 설치 위치를 여러 곳에 만들었다면 도구의 우선순위를 확인하세요.

```bash
python3 scripts/install.py --target claude --project /path/to/project --dry-run
```

이미 다른 내용의 `im-novelist` 폴더가 있으면 기본 설치가 중단됩니다. 기존 스킬을 업데이트하려면 저장소의 최신 버전을 받은 뒤 대상별로 `--update`를 추가하세요. 이전 폴더 전체는 같은 스킬 디렉터리 안의 숨김 백업 폴더에 보관하고 경로를 출력합니다. 다른 스킬이거나 심볼릭 링크인 경우에는 교체하지 않습니다. `--destination /exact/path/im-novelist`로 다른 정확한 위치를 지정할 수도 있습니다.

```bash
git pull --ff-only
python3 scripts/install.py --target claude --update
python3 scripts/install.py --target gemini --update
python3 scripts/install.py --target codex --update
```

## 선택형 검토

제한과 공고 기준이 있을 때 다음처럼 요청할 수 있습니다.

```text
아래 지원서를 다듬어줘. 대표 문장 두 개의 목소리를 살리고,
본문은 UTF-8 기준 1,000바이트 이내야. 공백과 LF 줄바꿈을 포함해줘.
학교명과 내가 제공한 금지 명칭도 공고 기준으로 점검해줘.
```

바이트를 직접 확인하려면 UTF-8 텍스트 파일로 저장한 최종 원고와 제출처의 기준을 사용합니다.

```bash
python3 scripts/count_text.py 원고.txt --encoding utf-8 --newlines lf --max-bytes 1000
```

원문 줄바꿈을 유지하려면 `--newlines preserve`, CRLF로 계산하려면 `--newlines crlf`를 지정합니다. 공백과 마지막 줄바꿈, 입력에 있는 UTF-8 BOM은 계산에 포함합니다. 제출처마다 바이트·줄바꿈 기준이 다를 수 있으며, 자체 환산 규칙은 해당 시스템에서 따로 확인해야 합니다. 블라인드 최종 판정은 채용기관 기준에 따릅니다. 사실 검증과 문서의 시각적 배치 검사도 실제 자료와 최종 파일을 확인한 범위만 보고합니다.

## 구조

| 경로 | 용도 |
| --- | --- |
| [SKILL.md](SKILL.md) | 공통 지침과 작업 순서 |
| [references](references) | 패턴·의미·목소리, 긴 글·지원서 예시와 선택형 검사 절차 |
| [prompts/im-novelist.md](prompts/im-novelist.md) | 파일 접근이 없는 대화창용 독립 프롬프트 |
| [docs/compatibility.md](docs/compatibility.md) | 서비스별 설치와 사용 범위 |
| [docs/research.md](docs/research.md) | 출처, 근거의 범위, 설계에 반영한 판단 |
| [docs/evaluation.md](docs/evaluation.md) | 평가 방법과 검증 범위 |
| [evals/cases.json](evals/cases.json) | 의미 보존·말투·모호함에 대한 사례 |
| [scripts](scripts) | 설치·바이트 계산·프롬프트 생성·구조 검사 |

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

English: A provider-neutral Korean prose editing skill. Install the Agent Skills package in Claude Code, Gemini CLI, or Codex, or paste `prompts/im-novelist.md` into a chat. Preserve meaning and voice; edit formulaic phrasing in context.
