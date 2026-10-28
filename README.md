# im-poetry

원문의 뜻과 목소리를 지키며 한국어 AI 문체를 다듬는 공용 스킬입니다.

Claude, Gemini, GPT에서 같은 편집 원칙을 사용할 수 있습니다. Agent Skills를 지원하는 도구에는 스킬 폴더를 설치하고, 일반 대화창에는 독립 프롬프트를 붙여 넣습니다. 사용에 API 키나 외부 서비스는 필요하지 않습니다.

## 어떤 글을 다듬나요?

- 말만 바꾸어 반복하는 문장과 문단
- 과장된 도입, 상투적인 감상, 불필요한 마무리
- 동작을 감춘 명사 나열과 불분명한 연결
- 글의 목적과 맞지 않는 획일적인 호흡과 말투

'있다', '것', '수 있다', 부사, 피동문을 금칙어로 취급하지 않습니다. 가능성, 시간, 감정, 인용, 수치, 코드처럼 보존해야 할 내용을 먼저 확인합니다. 에세이·메시지·지원서·보고서·기술 설명을 각각의 목적에 맞게 다듬습니다.

긴 글은 대표 문장과 여러 문단의 흐름을 함께 살핍니다. 영향이나 기여를 더 강한 원인으로 바꾸지 않고, 과거 평가 결과를 미래 성능으로 확대하지 않습니다. 분량·블라인드·사실·문서 배치 검사는 요청이나 해당 조건이 있을 때만 추가합니다.

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

Python 3.10 이상이 필요합니다. 실행 전 코드를 확인할 수 있으며, 설치기는 네트워크를 사용하지 않습니다. 기본 설치에서는 기존 스킬이나 설정 파일을 덮어쓰지 않습니다.

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

이미 다른 내용의 `im-poetry` 폴더가 있으면 기본 설치가 중단됩니다. 기존 스킬을 업데이트하려면 저장소의 최신 버전을 받은 뒤 대상별로 `--update`를 추가하세요. 이전 폴더 전체는 같은 스킬 디렉터리 안의 숨김 백업 폴더에 보관하고 경로를 출력합니다. 다른 스킬이거나 심볼릭 링크인 경우에는 교체하지 않습니다. `--destination /exact/path/im-poetry`로 다른 정확한 위치를 지정할 수도 있습니다.

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
| [references](references) | 패턴·의미·목소리, 긴 글 예시와 선택형 검사 절차 |
| [prompts/im-poetry.md](prompts/im-poetry.md) | 파일 접근이 없는 대화창용 독립 프롬프트 |
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

English: A provider-neutral Korean prose editing skill. Install the Agent Skills package in Claude Code, Gemini CLI, or Codex, or paste `prompts/im-poetry.md` into a chat. Preserve meaning and voice; edit formulaic phrasing in context.
