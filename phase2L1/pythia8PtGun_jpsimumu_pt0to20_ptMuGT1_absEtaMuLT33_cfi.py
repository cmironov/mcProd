import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("Pythia8PtGun",
                          PGunParameters = cms.PSet(
                             AddAntiParticle = cms.bool(False),
                             MinEta = cms.double(-3.0),
                             MaxEta = cms.double(3.0),
                             MinPhi          = cms.double(-3.14159265359),
                             MaxPhi          = cms.double(3.14159265359),
                             MinPt           = cms.double(0.0),
                             MaxPt           = cms.double(20.0),
                             ParticleID      = cms.vint32(443)
                             ),
                          PythiaParameters = cms.PSet(
                              jpsiDecay = cms.vstring('443:onMode  = off',  # turn off all decays
                                                      '443:onIfAny = 13 -13'),
                              parameterSets = cms.vstring('jpsiDecay')
                              ),
                          Verbosity = cms.untracked.int32(0)
                        )
                        
mumugenfilter = cms.EDFilter("MCParticlePairFilter",
                             Status = cms.untracked.vint32(1, 1),
                             MinPt = cms.untracked.vdouble(1., 1.),
                             MaxEta = cms.untracked.vdouble(3.0, 3.0),
                             MinEta = cms.untracked.vdouble(-3.0, -3.0),
                             ParticleCharge = cms.untracked.int32(0),
                             ParticleID1 = cms.untracked.vint32(13),
                             ParticleID2 = cms.untracked.vint32(13)
                            )

ProductionFilterSequence  = cms.Sequence(generator+mumugenfilter)



