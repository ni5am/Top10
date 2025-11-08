<link rel="stylesheet" href="../assets/css/RC-stylesheet.css" />

# A04:2025 암호화 실패 (Cryptographic Failures) 



## 배경 (Background). 

순위에서 두 단계 하락하여 #4로 이동한 이 약점은 암호화 부족, 충분히 강력하지 않은 암호화, 암호화 키 누출 및 관련 오류와 관련된 실패에 초점을 맞춥니다. 이 위험에서 가장 일반적인 공통 취약점 열거(Common Weakness Enumerations, CWE) 중 세 가지는 약한 의사 난수 생성기 사용과 관련이 있습니다: *CWE-327 깨진 또는 위험한 암호화 알고리즘 사용 (Use of a Broken or Risky Cryptographic Algorithm), CWE-331: 엔트로피 부족 (Insufficient Entropy)*, *CWE-1241: 난수 생성기에서 예측 가능한 알고리즘 사용 (Use of Predictable Algorithm in Random Number Generator)*, *CWE-338 암호학적으로 약한 의사 난수 생성기(PRNG) 사용 (Use of Cryptographically Weak Pseudo-Random Number Generator, PRNG)*.



## 점수 표 (Score table).


<table>
  <tr>
   <td>매핑된 CWE (CWEs Mapped) 
   </td>
   <td>최대 발생률 (Max Incidence Rate)
   </td>
   <td>평균 발생률 (Avg Incidence Rate)
   </td>
   <td>최대 커버리지 (Max Coverage)
   </td>
   <td>평균 커버리지 (Avg Coverage)
   </td>
   <td>평균 가중 악용 (Avg Weighted Exploit)
   </td>
   <td>평균 가중 영향 (Avg Weighted Impact)
   </td>
   <td>총 발생 횟수 (Total Occurrences)
   </td>
   <td>총 CVE (Total CVEs)
   </td>
  </tr>
  <tr>
   <td>32
   </td>
   <td>13.77%
   </td>
   <td>3.80%
   </td>
   <td>100.00%
   </td>
   <td>47.74%
   </td>
   <td>7.23
   </td>
   <td>3.90
   </td>
   <td>1,665,348
   </td>
   <td>2,185
   </td>
  </tr>
</table>



## 설명 (Description). 

일반적으로 전송 중인 모든 데이터는 [전송 계층 (transport layer)](https://en.wikipedia.org/wiki/Transport_layer) ([OSI 계층 (OSI layer)](https://en.wikipedia.org/wiki/OSI_model) 4)에서 암호화되어야 합니다. CPU 성능 및 개인 키/인증서 관리와 같은 이전 장애물은 이제 암호화를 가속화하도록 설계된 명령어를 가진 CPU(예: [AES 지원](https://en.wikipedia.org/wiki/AES_instruction_set))와 [LetsEncrypt.org](https://LetsEncrypt.org)와 같은 서비스에 의해 개인 키 및 인증서 관리가 단순화되고 주요 클라우드 벤더가 특정 플랫폼에 대해 더욱 긴밀하게 통합된 인증서 관리 서비스를 제공함으로써 처리됩니다. 

전송 계층을 보안하는 것 외에도, 저장 시 암호화가 필요한 데이터와 전송 중 추가 암호화가 필요한 데이터([애플리케이션 계층 (application layer)](https://en.wikipedia.org/wiki/Application_layer), OSI 계층 7)를 결정하는 것이 중요합니다. 예를 들어, 암호, 신용 카드 번호, 건강 기록, 개인 정보 및 비즈니스 비밀은 추가 보호가 필요하며, 특히 해당 데이터가 개인정보 보호법(예: EU의 일반 데이터 보호 규정(General Data Protection Regulation, GDPR)) 또는 PCI 데이터 보안 표준(PCI Data Security Standard, PCI DSS)과 같은 규정에 해당하는 경우 그렇습니다. 이러한 모든 데이터에 대해:



* 기본값으로 또는 이전 코드에서 오래되었거나 약한 암호화 알고리즘 또는 프로토콜이 사용되고 있습니까?
* 기본 암호화 키가 사용 중이거나, 약한 암호화 키가 생성되거나, 키가 재사용되거나, 적절한 키 관리 및 순환이 누락되어 있습니까? 
* 암호화 키가 소스 코드 저장소에 체크인되어 있습니까?
* 암호화가 강제되지 않습니까? 예: HTTP 헤더(브라우저) 보안 지시문 또는 헤더가 누락되어 있습니까?
* 수신된 서버 인증서와 신뢰 체인이 적절하게 검증되고 있습니까?
* 초기화 벡터가 무시되거나 재사용되거나 암호화 작동 모드에 대해 충분히 안전하게 생성되지 않습니까? ECB와 같은 불안전한 작동 모드가 사용 중입니까? 인증된 암호화가 더 적절한 경우 암호화가 사용되고 있습니까?
* 암호 기반 키 파생 함수가 없는 경우 암호가 암호화 키로 사용되고 있습니까?
* 암호화 요구 사항을 충족하도록 설계되지 않은 난수가 암호화 목적으로 사용되고 있습니까? 올바른 함수가 선택되었더라도, 개발자가 시드해야 하며, 그렇지 않은 경우 개발자가 내장된 강력한 시딩 기능을 엔트로피/예측 불가능성이 부족한 시드로 덮어썼습니까?
* MD5 또는 SHA1과 같은 사용 중단된 해시 함수가 사용 중이거나, 암호화 해시 함수가 필요한 경우 비암호화 해시 함수가 사용되고 있습니까?
* PKCS 번호 1 v1.5와 같은 사용 중단된 암호화 패딩 방법이 사용되고 있습니까?
* 암호화 오류 메시지 또는 사이드 채널 정보가 악용 가능합니까? 예: 패딩 오라클 공격의 형태로?
* 암호화 알고리즘이 다운그레이드되거나 우회될 수 있습니까?

참고 자료 ASVS: 암호화(Cryptography, V11), 보안 통신(Secure Communication, V12) 및 데이터 보호(Data Protection, V14)를 참조하세요.


## 예방 방법 (How to prevent). 

최소한 다음을 수행하고 참고 자료를 참조하세요:



* 애플리케이션이 처리, 저장 또는 전송하는 데이터를 분류하고 레이블을 지정하세요. 개인정보 보호법, 규제 요구 사항 또는 비즈니스 요구에 따라 민감한 데이터를 식별하세요.
* 가장 민감한 키를 하드웨어 또는 클라우드 기반 HSM에 저장하세요.
* 가능할 때마다 잘 신뢰할 수 있는 암호화 알고리즘 구현을 사용하세요.
* 불필요하게 민감한 데이터를 저장하지 마세요. 가능한 한 빨리 폐기하거나 PCI DSS 호환 토큰화 또는 심지어 잘라내기를 사용하세요. 보관되지 않은 데이터는 도난당할 수 없습니다.
* 저장 시 모든 민감한 데이터를 암호화해야 합니다.
* 최신이고 강력한 표준 알고리즘, 프로토콜 및 키가 제자리에 있는지 확인하세요. 적절한 키 관리를 사용하세요.
* 전달 비밀(Forward Secrecy, FS) 암호, 서버에 의한 암호 우선순위 지정 및 안전한 매개변수를 사용하여 TLS와 같은 안전한 프로토콜로 전송 중인 모든 데이터를 암호화하세요. HTTP Strict Transport Security (HSTS)와 같은 지시문을 사용하여 암호화를 강제하세요.
* 민감한 데이터를 포함하는 응답에 대한 캐싱을 비활성화하세요. 여기에는 CDN, 웹 서버 및 모든 애플리케이션 캐싱(예: Redis)의 캐싱이 포함됩니다.
* 데이터 분류에 따라 필요한 보안 제어를 적용하세요.
* FTP 및 SMTP와 같은 암호화되지 않은 프로토콜을 사용하지 마세요.
* Argon2, scrypt, bcrypt(레거시 시스템) 또는 PBKDF2-HMAC-SHA-256과 같은 작업 요소(지연 요소)가 있는 강력한 적응형 및 솔트 해시 함수를 사용하여 암호를 저장하세요. bcrypt를 사용하는 레거시 시스템의 경우 [OWASP 치트 시트: 암호 저장 (OWASP Cheat Sheet: Password Storage)](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)에서 더 많은 조언을 얻으세요.
* 초기화 벡터는 작동 모드에 적합하게 선택되어야 합니다. 이것은 CSPRNG(암호학적으로 안전한 의사 난수 생성기)를 사용하는 것을 의미할 수 있습니다. nonce가 필요한 모드의 경우, 초기화 벡터(IV)는 CSPRNG가 필요하지 않습니다. 모든 경우에 IV는 고정 키에 대해 두 번 사용되어서는 안 됩니다.
* 항상 단순한 암호화 대신 인증된 암호화를 사용하세요.
* 키는 암호학적으로 무작위로 생성되어야 하며 바이트 배열로 메모리에 저장되어야 합니다. 암호가 사용되는 경우, 적절한 암호 기반 키 파생 함수를 통해 키로 변환되어야 합니다.
* 암호화 난수가 적절한 곳에서 사용되고 예측 가능한 방식이나 낮은 엔트로피로 시드되지 않았는지 확인하세요. 대부분의 현대 API는 개발자가 CSPRNG를 시드할 필요가 없어도 안전합니다.
* MD5, SHA1, 암호 블록 체이닝 모드(Cipher Block Chaining Mode, CBC), PKCS 번호 1 v1.5와 같은 사용 중단된 암호화 함수, 블록 구축 방법 및 패딩 방식을 피하세요.
* 보안 전문가, 이를 위해 설계된 도구 또는 둘 다에 의해 검토되도록 설정 및 구성이 보안 요구 사항을 충족하는지 확인하세요.
* 양자 후 암호화(Post Quantum Cryptography, PQC)를 준비하는 것을 고려하세요. 참고 자료(ENISA, NIST)를 참조하세요.


## 공격 시나리오 예 (Example attack scenarios). 

**시나리오 #1**: 사이트가 모든 페이지에 대해 TLS를 사용하거나 강제하지 않거나 약한 암호화를 지원합니다. 공격자는 네트워크 트래픽을 모니터링하고(예: 불안전한 무선 네트워크에서), 연결을 HTTPS에서 HTTP로 다운그레이드하고, 요청을 가로채고, 사용자의 세션 쿠키를 훔칩니다. 그런 다음 공격자는 이 쿠키를 재생하고 사용자의 (인증된) 세션을 탈취하여 사용자의 프라이빗 데이터에 액세스하거나 수정합니다. 위의 대신 전송된 모든 데이터를 변경할 수 있습니다. 예: 송금 수신인.

**시나리오 #2**: 암호 데이터베이스가 솔트 없이 또는 간단한 해시를 사용하여 모든 사람의 암호를 저장합니다. 파일 업로드 결함으로 인해 공격자가 암호 데이터베이스를 검색할 수 있습니다. 모든 솔트 없는 해시는 사전 계산된 해시의 레인보우 테이블로 노출될 수 있습니다. 간단하거나 빠른 해시 함수로 생성된 해시는 솔트가 있었더라도 GPU로 크래킹될 수 있습니다.


## 참고 자료 (References).



* [OWASP 사전 대응 제어: C2: 데이터 보호를 위해 암호화 사용 (OWASP Proactive Controls: C2: Use Cryptography to Protect Data)](https://top10proactive.owasp.org/archive/2024/the-top-10/c2-crypto/)
* [OWASP 애플리케이션 보안 검증 표준 (ASVS): ](https://owasp.org/www-project-application-security-verification-standard) [V11,](https://github.com/OWASP/ASVS/blob/v5.0.0/5.0/en/0x20-V11-Cryptography.md) [12, ](https://github.com/OWASP/ASVS/blob/v5.0.0/5.0/en/0x21-V12-Secure-Communication.md) [14](https://github.com/OWASP/ASVS/blob/v5.0.0/5.0/en/0x23-V14-Data-Protection.md)
* [OWASP 치트 시트: 전송 계층 보호 (OWASP Cheat Sheet: Transport Layer Protection)](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
* [OWASP 치트 시트: 사용자 개인정보 보호 (OWASP Cheat Sheet: User Privacy Protection)](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)
* [OWASP 치트 시트: 암호 저장 (OWASP Cheat Sheet: Password Storage)](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [OWASP 치트 시트: 암호화 저장소 (OWASP Cheat Sheet: Cryptographic Storage)](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
* [OWASP 치트 시트: HSTS](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html)
* [OWASP 테스트 가이드: 약한 암호화 테스트 (OWASP Testing Guide: Testing for weak cryptography)](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/README)
* [ENISA: 양자 후 암호화로의 전환을 위한 조정된 구현 로드맵 (ENISA: A Coordinated Implementation Roadmap for the Transition to Post-Quantum Cryptography)](https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography)
* [NIST 첫 3개의 최종 양자 후 암호화 표준 발표 (NIST Releases First 3 Finalized Post-Quantum Encryption Standards)](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)


## 매핑된 CWE 목록 (List of Mapped CWEs)

* [CWE-261 암호에 대한 약한 인코딩 (Weak Encoding for Password)](https://cwe.mitre.org/data/definitions/261.html)

* [CWE-296 인증서의 신뢰 체인을 부적절하게 따름 (Improper Following of a Certificate's Chain of Trust)](https://cwe.mitre.org/data/definitions/296.html)

* [CWE-319 민감한 정보의 평문 전송 (Cleartext Transmission of Sensitive Information)](https://cwe.mitre.org/data/definitions/319.html)

* [CWE-320 키 관리 오류 (금지됨) (Key Management Errors (Prohibited))](https://cwe.mitre.org/data/definitions/320.html)

* [CWE-321 하드코딩된 암호화 키 사용 (Use of Hard-coded Cryptographic Key)](https://cwe.mitre.org/data/definitions/321.html)

* [CWE-322 엔티티 인증 없이 키 교환 (Key Exchange without Entity Authentication)](https://cwe.mitre.org/data/definitions/322.html)

* [CWE-323 암호화에서 Nonce, 키 쌍 재사용 (Reusing a Nonce, Key Pair in Encryption)](https://cwe.mitre.org/data/definitions/323.html)

* [CWE-324 만료일이 지난 키 사용 (Use of a Key Past its Expiration Date)](https://cwe.mitre.org/data/definitions/324.html)

* [CWE-325 필수 암호화 단계 누락 (Missing Required Cryptographic Step)](https://cwe.mitre.org/data/definitions/325.html)

* [CWE-326 불충분한 암호화 강도 (Inadequate Encryption Strength)](https://cwe.mitre.org/data/definitions/326.html)

* [CWE-327 깨진 또는 위험한 암호화 알고리즘 사용 (Use of a Broken or Risky Cryptographic Algorithm)](https://cwe.mitre.org/data/definitions/327.html)

* [CWE-328 가역적 일방향 해시 (Reversible One-Way Hash)](https://cwe.mitre.org/data/definitions/328.html)

* [CWE-329 CBC 모드에서 랜덤 IV를 사용하지 않음 (Not Using a Random IV with CBC Mode)](https://cwe.mitre.org/data/definitions/329.html)

* [CWE-330 불충분하게 랜덤한 값 사용 (Use of Insufficiently Random Values)](https://cwe.mitre.org/data/definitions/330.html)

* [CWE-331 엔트로피 부족 (Insufficient Entropy)](https://cwe.mitre.org/data/definitions/331.html)

* [CWE-332 PRNG의 엔트로피 부족 (Insufficient Entropy in PRNG)](https://cwe.mitre.org/data/definitions/332.html)

* [CWE-334 작은 랜덤 값 공간 (Small Space of Random Values)](https://cwe.mitre.org/data/definitions/334.html)

* [CWE-335 의사 난수 생성기(PRNG)에서 시드의 잘못된 사용 (Incorrect Usage of Seeds in Pseudo-Random Number Generator(PRNG))](https://cwe.mitre.org/data/definitions/335.html)

* [CWE-336 의사 난수 생성기(PRNG)에서 동일한 시드 (Same Seed in Pseudo-Random Number Generator (PRNG))](https://cwe.mitre.org/data/definitions/336.html)

* [CWE-337 의사 난수 생성기(PRNG)에서 예측 가능한 시드 (Predictable Seed in Pseudo-Random Number Generator (PRNG))](https://cwe.mitre.org/data/definitions/337.html)

* [CWE-338 암호학적으로 약한 의사 난수 생성기(PRNG) 사용 (Use of Cryptographically Weak Pseudo-Random Number Generator(PRNG))](https://cwe.mitre.org/data/definitions/338.html)

* [CWE-340 예측 가능한 숫자 또는 식별자 생성 (Generation of Predictable Numbers or Identifiers)](https://cwe.mitre.org/data/definitions/340.html)

* [CWE-342 이전 값에서 예측 가능한 정확한 값 (Predictable Exact Value from Previous Values)](https://cwe.mitre.org/data/definitions/342.html)

* [CWE-347 암호화 서명의 부적절한 검증 (Improper Verification of Cryptographic Signature)](https://cwe.mitre.org/data/definitions/347.html)

* [CWE-523 자격 증명의 보호되지 않은 전송 (Unprotected Transport of Credentials)](https://cwe.mitre.org/data/definitions/523.html)

* [CWE-757 협상 중 덜 안전한 알고리즘 선택('알고리즘 다운그레이드', Selection of Less-Secure Algorithm During Negotiation('Algorithm Downgrade'))](https://cwe.mitre.org/data/definitions/757.html)

* [CWE-759 솔트 없이 일방향 해시 사용 (Use of a One-Way Hash without a Salt)](https://cwe.mitre.org/data/definitions/759.html)

* [CWE-760 예측 가능한 솔트를 사용한 일방향 해시 사용 (Use of a One-Way Hash with a Predictable Salt)](https://cwe.mitre.org/data/definitions/760.html)

* [CWE-780 OAEP 없이 RSA 알고리즘 사용 (Use of RSA Algorithm without OAEP)](https://cwe.mitre.org/data/definitions/780.html)

* [CWE-916 계산 노력이 불충분한 암호 해시 사용 (Use of Password Hash With Insufficient Computational Effort)](https://cwe.mitre.org/data/definitions/916.html)

* [CWE-1240 위험한 구현을 가진 암호화 기본 요소 사용 (Use of a Cryptographic Primitive with a Risky Implementation)](https://cwe.mitre.org/data/definitions/1240.html)

* [CWE-1241 난수 생성기에서 예측 가능한 알고리즘 사용 (Use of Predictable Algorithm in Random Number Generator)](https://cwe.mitre.org/data/definitions/1241.html)
